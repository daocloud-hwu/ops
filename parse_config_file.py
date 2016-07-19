#!/usr/bin/python

import yaml
import sys

if len(sys.argv) < 3:
  sys.exit(1)

for yml in sys.argv[2:]:
  for svc, content in yaml.load(open(yml, "r")).items():
    prefix = "constraint:node=="
    node = ""
    for env in content.get("environment", []):
      if env.startswith(prefix):
        node = env[len(prefix):]
        break
    for vol in content.get("volumes", []):
      if sys.argv[1]+":" in vol:
        print svc, node, vol.split(":")[0]
