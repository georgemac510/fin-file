from __future__ import print_function


import fmt
import io

import random
import logging
import struct

import grpc
import buckets_pb2_grpc
import buckets_pb2
from dataclasses import dataclass

@dataclass
class Client:
    c: pb.APIClient
    conn: *grpc.ClientConn


    

def NewClient((target string, opts ...grpc.DialOption) (*Client, error) {
	conn, err := grpc.Dial(target, opts...)):
    return buckets_pb2.NewClient(
        return Client(c=pb.NewAPIClient(conn),conn=conn)

def (c *Client) Close (channel, error):
    c.conn.Close() 

def (c *Client) Init(ctx context.Context, opts ...InitOption) (*pb.InitReply, error):
    args = initOptions()
    if opt=range.opts(opt(args)):
        print(strCid = args.fromCid.String())
        return c.c.Init(ctx, &pb.InitRequest (
            Name:         args.name,
            Private:      args.private,
            BootstrapCid: strCid
        )
def (c *Client) Root(ctx context.Context, key string) (*pb.RootReply, error):
    return c.c.Root(ctx, &pb.RootRequest(Key: key))

def (c *Client) Links(ctx context.Context, key string) (*pb.LinksReply, error):
	return c.c.Links(ctx, &pb.LinksRequest(Key: key))

def (c *Client) List(ctx context.Context) (*pb.ListReply, error):
	return c.c.List(ctx, &pb.ListRequest())
		
def (c *Client) ListIpfsPath(ctx context.Context, pth path.Path) (*pb.ListIpfsPathReply, error):
	return c.c.ListIpfsPath(ctx, &pb.ListIpfsPathRequest(Path: pth.String()))

def (c *Client) ListPath(ctx context.Context, key, pth string) (*pb.ListPathReply, error): 
	return c.c.ListPath(ctx, &pb.ListPathRequest(
		Key:  key,
		Path: pth
	))

def (c *Client) SetPath(ctx context.Context, key, pth string, remoteCid cid.Cid) (*pb.SetPathReply, error):
	return c.c.SetPath(ctx, &pb.SetPathRequest(
		Key:  key,
		Path: pth,
		Cid:  remoteCid.String()
	)

@dataclass
class pushPathResult:
    path: path.Resolved
	root: path.Resolved
	err:  error


def generate_route(feature_list):
    for _ in range(0, 10):
        random_feature = feature_list[random.randint(0, len(feature_list) - 1)]
        print("Visiting point %s" % random_feature.location)
        yield random_feature.location


def guide_record_route(stub):
    feature_list = route_guide_resources.read_route_guide_database()

    route_iterator = generate_route(feature_list)
    route_summary = stub.RecordRoute(route_iterator)
    print("Finished trip with %s points " % route_summary.point_count)
    print("Passed %s features " % route_summary.feature_count)
    print("Travelled %s meters " % route_summary.distance)
    print("It took %s seconds " % route_summary.elapsed_time)


def generate_messages():
    messages = [
        make_route_note("First message", 0, 0),
        make_route_note("Second message", 0, 1),
        make_route_note("Third message", 1, 0),
        make_route_note("Fourth message", 0, 0),
        make_route_note("Fifth message", 1, 0),
    ]
    for msg in messages:
        print("Sending %s at %s" % (msg.message, msg.location))
        yield msg


def guide_route_chat(stub):
    responses = stub.RouteChat(generate_messages())
    for response in responses:
        print("Received message %s at %s" %
              (response.message, response.location))


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        print("-------------- GetFeature --------------")
        guide_get_feature(stub)
        print("-------------- ListFeatures --------------")
        guide_list_features(stub)
        print("-------------- RecordRoute --------------")
        guide_record_route(stub)
        print("-------------- RouteChat --------------")
        guide_route_chat(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()