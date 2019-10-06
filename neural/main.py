#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: penghuailiang
# @Date  : 2019-09-20

import tensorflow as tf
from parse import parser
from model import Artgan, Face
from net import Net

import logging
logger = logging.getLogger("nn-face")

tf.set_random_seed(228)


def main(_):
    args = parser.parse_args()

    with tf.Session() as sess:
        model = Face(sess, args)
        if args.phase == "train":
            model.train(args)
            print ('train mode')


    # net = Net(5010, 5011)
    #
    # while True:
    #     input = raw_input("command: \n")
    #     if input == "s":
    #         msg = raw_input("input: ")
    #         net.only_send(msg)
    #     elif input == 'r':
    #         msg = raw_input("input: ")
    #         net.send_recv(msg)
    #     elif input == "q":
    #         net.only_send("quit")
    #         net.close()
    #         break
    #     else:
    #         logger.info("unknown code, quit")
    #         net.close()
    #         break


if __name__ == '__main__':
    tf.app.run()
