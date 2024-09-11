# Time-stamp: <2022-01-04 11:13:21 christophe@pallier.org>
# generate html slides from markdown (see https://pypi.org/project/darkslide/)

SOURCES := $(wildcard *.md)

all: $(SOURCES:.md=.html)

%.html: %.md
	darkslide -x tables --embed --relative -l table $< -d $@
