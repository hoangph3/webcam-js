SHELL := /bin/bash

VERSION := 1.0.0
OS := $(shell uname -m)

WEBCAM_IMG = hoangph3/facekyc-webcam-js

build: 
	docker build -t $(WEBCAM_IMG):$(OS)-$(VERSION) .
