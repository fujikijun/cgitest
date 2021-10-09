#!/usr/local/bin/perl

@aaa = ("佐藤\n","竹内\n","近藤\n");

my $fh_log;
my $ymd;
my $hms;

$ymd = get_date("LFM");         # 日付取得
$hms = get_time("LFM");         # 時間取得
printf($fh_log,"> %s%s.txt", $ymd, $hms, $logmsg);

open (OUT,$fh_log);
print OUT @aaa;
close (OUT);

exit;