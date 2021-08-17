import argparse
from Secure_Server import secure_server_start
from Secure_Client import secure_client_start
from Server import unsecure_server_start
from Client import unsecure_client_start
from MITM import mitm_start

parser = argparse.ArgumentParser(description='Choose whether to run a client or a server, and whether it should be secure or not')
parser.add_argument('--tls', action='store_true', help='run secure server')
parser.add_argument('--mitm', action='store_true', help='run man in the middle')
group = parser.add_mutually_exclusive_group()
group.add_argument('--server', action='store_true', help='run server')
group.add_argument('--client', action='store_true', help='run client')
args = parser.parse_args()

if __name__ == '__main__':
  if args.mitm:
    # run man in the middle
    mitm_start()
  if args.tls:
    if args.server:
      # run secure server
      # secure_server_start("9999")
      secure_server_start()
    elif args.client:
      # run secure client
      # secure_client_start("localhost", "9999")
      secure_client_start()
  else:
    if args.server:
      # run unsecure server
      unsecure_server_start()
    elif args.client:
      # run unsecure client
      unsecure_client_start()