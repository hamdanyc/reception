#!/usr/bin/awk -f

BEGIN{seat=1; table=1; FS=","; print "name,seat,table"}
NR==1 {next}  # Skip the first row
{print $1","seat","table}
{seat++; if (NR % 10 == 1) {seat=1; table++}}
{next}
