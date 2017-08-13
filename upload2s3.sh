#!/bin/bash

cd /root/venv34
source bin/activate

python upload2dirS3.py /var/lib/psa/dumps maravishbackups `date +"backup%Ysem%V"`
