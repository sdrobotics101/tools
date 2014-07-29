#!/usr/bin/perl

use strict;

my @l1_vals = ();
my @l2_vals = ();

while (<STDIN>) {
	chop;
	my @words = split(/\s+/,$_,9999);

	if (($words[0] eq "S:") && ($#words==13)) {
		push(@l1_vals, $words[2], $words[3], $words[4]);
	}
	elsif (($words[0] eq "M:") && ($#words==21)) {
		push(@l2_vals, $words[2], $words[3], $words[4]);
		print join(" ", @l1_vals, @l2_vals) . "\n"; 
                @l1_vals = (); @l2_vals = ();
	}
}
