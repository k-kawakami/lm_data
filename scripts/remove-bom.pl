#!/usr/bin/perl -w
use strict;
while(<>) {
  s/ \xEF\xBB\xBF / /g;
  die if /\xEF\xBB\xBF/;
  print;
}
