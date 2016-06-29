#!/usr/bin/python

import yaml
import sys

if len(sys.argv) != 2:
  sys.exit(1)

for _, content in yaml.load(open(sys.argv[1], "r")).items():
  prefix = "constraint:node=="
  image = content["image"]
  node = ""
  for env in content["environment"]:
    if env.startswith(prefix):
      node = env[len(prefix):]
      break
  print node, image
