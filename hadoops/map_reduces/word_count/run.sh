#!/bin/bash/
hadoop fs -rm -r -f /test/output/wordcount

hadoop jar /home/hadoop/apps/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file mapper.py \
-file reducer.py \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py" \
-input /test/input/words.text \
-output /test/output/wordcount