---
title: "Fast ADC with an Arduino Yun"
categories: blog
layout: post-light-feature
date:   2016-01-26 15:00:00
keywords: arduino, c++, python, serial, udp, hardware, firmware, software
long_title: true
---

# Fast ADC with an Arduino Yun

Code (software and firmware) at
[github:alexhagen:fast_adc_yun](http://github.com/alexhagen/fast_adc_yun)

I've created a fast analog to digital conversion system using only an Arduino
Yun (and an external computer to process data).  The system can sample the
Arduino Yun's ADC at 8-bit at greater than 30 kSps and then send those samples
out via UDP at the same rate.  With a fast enough external computer (most modern
computers would be), you can then catch most of those samples without error and
plot them, or log them.

## Motivation
