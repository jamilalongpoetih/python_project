import pyshark
import argparse
import sys
import os
from datetime import datetime

def start_capture():
	#Setup the parser
	parser=argparse.ArgumentParser(description='Live Packet Capture Tool')
	parser.add_argument('-i','--interface',required=True,help='The network interface to monitor')
	parser.add_argument('-o','--output',help='file to save packets')
	parser.add_argument('-c','--count',type=int,required=True,help='number of packets to capture')
	args=parser.parse_args()

	interface_name=args.interface
	target_count=args.count
	timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
	file_name = f"capture{target_count}_{timestamp}.pcap"

	capture = pyshark.LiveCapture(interface=interface_name,output_file=file_name)
	#the following function runs when CTL-C is typed
	print(f"-- Capturing Traffic on {interface_name} and saving to {file_name} --")
	print(f"-- Capture {target_count} packets and save to {file_name} --")
	try:
		#sniff_continuously until you stop with <Ctl-C> 
		for i, packet in enumerate(capture.sniff_continuously(packet_count=target_count)):
			print(f"\n{i+1}/{target_count} Captured: {packet.highest_layer}")
			if 'ARP' in packet:
				print(f"   (ARP):  {packet.arp.src_hw_mac} is looking for {packet.arp.dst_proto_ipv4}")
			#next one always exists 
			print(f"Layer 2 (Link): {packet.eth.src} -> {packet.eth.dst}")
			if 'IP' in packet:
				print(f"Layer 3 (Network): {packet.ip.src} -> {packet.ip.dst}")
			#checks if the packet has a Transport Layer frame (TCP/UDP)
			if packet.transport_layer is not None:
				t_layer = packet.transport_layer.lower()
				print(f"Layer 4 (Transport): {packet.transport_layer} port {packet[packet.transport_layer].dstport}")
			else:
				print("    Transport: None (Non-IP/UDP/TCP packet)")

			print(f"Layer 7 (Application): {packet.highest_layer}")
	
	except Exception as e:
		print(f"Error occurred: {e}")
	
	finally:
		capture.close()
		print(f"-- Done. {target_count} packets saved to {file_name} --")
		os._exit(0)
				
if __name__ == "__main__":
	start_capture()
