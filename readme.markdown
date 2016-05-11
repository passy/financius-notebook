# Financius Notebook

A very basic analytics script for CSV exports out of
[Financius](https://play.google.com/store/apps/details?id=com.code44.finance).

![](screenshot.png)

## Disclaimer

This is highly tailored to my use and you probably won't get much out of this
unless you modify at least the categories to those that you use. Maybe the set
up and the more general income vs expenses stats are still useful for someone
other than me.

## Setup

You must be a masochist to install iPython locally on your system. I highly
advice to use docker instead.

```bash
docker run --rm -it -p 8888:8888 -v "$(pwd):/notebooks" jupyter/notebook
```

## How To Use

Export your financial data as CSV from Financius and download it into this
directory, so that you can access it from your Docker container.
