#!/usr/bin/perl

use strict;
use warnings;

my $wcpath = '/home/eromanowicz/bozenaromanowicz.com';
my $includefile = $wcpath.'/includes/revision.incl';

my $response;
my $rev;

$response = `/usr/bin/svn update $wcpath`;

print "Content-Type: text/plain\n";
print "Content-Language: en\n\n";
print "Result of update:\n\n";
print $response;

$rev = `/usr/bin/svnversion $wcpath`;
chomp $rev;

open REVINCLUDEFILE, '>'.$includefile or (print "Warning: Failed to update revision number!\n" and die);
print REVINCLUDEFILE ($rev);
close REVINCLUDEFILE;
