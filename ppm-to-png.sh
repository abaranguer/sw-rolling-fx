#!/bin/bash

for filename in $(ls -b ./processed-frames)
do
    convert ./processed-frames/"$filename" ./png/"$filename".png
done
echo "done!"
