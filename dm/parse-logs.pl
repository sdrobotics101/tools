#!/usr/bin/perl

use strict;

my @l1_vals = ();
my @l2_vals = ();

while (<STDIN>) {
	chop;
	my @words = split(/\s+/,$_,9999);

	if ($words[0] eq "S:") {
		push(@l1_vals, $words[1], $words[2], $words[3]);
	}
	elsif ($words[0] eq "M:") {
		push(@l2_vals, $words[1], $words[2], $words[3]);
		print join(" ", @l1_vals, @l2_vals); 
	}
}
