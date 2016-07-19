#!/bin/bash
ffmpeg -i png/frame_%05d.processed.ppm.png -c:v libx264 -pix_fmt yuv420p png/starwars-credits-fx.final.mp4
