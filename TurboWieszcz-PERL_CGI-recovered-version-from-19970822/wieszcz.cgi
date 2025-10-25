#!/usr/bin/perl
# MoNsTeR's/GDC PERL script Turbo Wieszcz++

### variables and setup

print "Content-type: text/html\n\n";

%val0 = ();
%val = ();
$meth=@ENV{"REQUEST_METHOD"};
$title="TurboWieszcz++";
$strof="4";
$rymy="ABAB";
@list1 = (); $sl1=0; @lastrnd1=();
@list2 = (); $sl2=0; @lastrnd2=();
@list3 = (); $sl3=0; @lastrnd3=();
@list4 = (); $sl4=0; @lastrnd4=();
@list5 = (); $sl5=0; @lastrnd5=();
$ref=@ENV{'HTTP_REFERER'};

 if ($meth eq "POST")
   { ### read STDIN and split into fields
    $xx = <STDIN>;
    @val0 = split("&",$xx);
    foreach $xx (@val0)
     {
      $word = $xx;
      $word =~ s/([\n\t\b\\;<>?\/*])//eg; ### more sec.?
      $word =~ s/\+/ /go;
      $word =~ s/<!--(.|\n)*-->//g;  ### security enhance?
      $word = &hex2asc ($word);
      push (@val, $word);
     }

    foreach $x (@val)
     {
      ($q1,$v)=split("=",$x);
      $v=~s/\</\&lt;/g; ### "<>"  -> &lt; &gt;
      $v=~s/\>/\&gt;/g;
      if ($q1 eq "title") {$title=$v};
      if ($q1 eq "strof") {$strof=$v};
      if ($q1 eq "rymy") {$rymy=$v};
     }
  }

$maxrym=$rymy;
srand;

open (BLA, "cat wieszcz.in |");
foreach $x (<BLA>)
{
 chop($x);
 ($sec,$txt)=split(":" ,$x);
 if ($sec eq 1) {push (@list1,$txt); $sl1++;}
 if ($sec eq 2) {push (@list2,$txt); $sl2++;}
 if ($sec eq 3) {push (@list3,$txt); $sl3++;}
 if ($sec eq 4) {push (@list4,$txt); $sl4++;}
 if ($sec eq 5) {push (@list5,$txt); $sl5++;}
}
close BLA;

### typ rymow...

   $rym = int(rand(10));
   $rymset1 = int(rand($maxrym)) + 1;
   $rymset2 = int(rand($maxrym)) + 1;
   if ($rymset1 eq $rymset2) {$rymset2++; if ($rymset2 > $maxrym) {$rymset2=0;} }

$s1="";$s2="";$s3="";$s4="";$s5="";$s6="";
if ($strof eq 1) {$s1=" SELECTED";}
elsif ($strof eq 2) {$s2=" SELECTED";}
elsif ($strof eq 3) {$s3=" SELECTED";}
elsif ($strof eq 4) {$s4=" SELECTED";}
elsif ($strof eq 5) {$s5=" SELECTED";}
elsif ($strof eq 6) {$s6=" SELECTED";}

$r1="";$r2="";
if ($rymy eq "AABB") {$r1=" SELECTED";} else {$r2=" SELECTED";}

print
"<html><HEAD><title>Wirtualna Pocztowka - TurboWieszcz++</title></HEAD>
<body bgcolor=\"#000000\" text=\"#ffffff\" link=\"#0000ff\" vlink=\"#0000ff\">
<CENTER>
<H1>Wirtualna Pocztowka Internetowa</H1>
<H2>TurboWieszcz++</H2>
<HR>

<FORM METHOD=\"POST\" ACTION=\"http://www.matrix.com.pl/~kuba/postcard/wieszcz.cgi\">
<INPUT TYPE=\"HIDDEN\" NAME=\"ref\" VALUE=\"\">
Tytul: <INPUT TYPE=\"TEXT\" NAME=\"title\" VALUE=\"$title\" SIZE=\"40\" MAXLENGTH=\"40\">
Strof: <SELECT NAME=\"strof\">
<OPTION VALUE=\"1\"$s1>1
<OPTION VALUE=\"2\"$s2>2
<OPTION VALUE=\"3\"$s3>3
<OPTION VALUE=\"4\"$s4>4
<OPTION VALUE=\"5\"$s5>5
<OPTION VALUE=\"6\"$s6>6
</SELECT>
Rymy: <SELECT NAME=\"rymy\">
<OPTION VALUE=\"AABB\"$r1>AABB
<OPTION VALUE=\"ABAB\"$r2>ABAB
</SELECT>

<INPUT TYPE=\"SUBMIT\" VALUE=\"WYGENERUJ!\"><INPUT TYPE=\"RESET\" VALUE=\"WYCZYSC...\">
</FORM>";

#print "<h3>REFERER: $ref</h3>\n\n";

print "<TABLE BORDER=0 CELLSPACING=2>\n";
if ($title ne "") {print "<TR><TD><h2>\"$title\"</h2></TD></TD>\n";}

for ($i=0;$i<$strof;$i++)
  {
   print "<TR><TD><B>";
   if ($rym ge 5)
     {
      &prt_rnd($rymset1,"");
      &prt_rnd($rymset2,"");
      &prt_rnd($rymset1,"");
      &prt_rnd($rymset2,".");
     }
   else
     {
      &prt_rnd($rymset1,"");
      &prt_rnd($rymset1,"");
      &prt_rnd($rymset2,"");
      &prt_rnd($rymset2,".");
     }
   print "</B></TD></TR>\n";
  }

print
"</TABLE></CNTER><HR>
<CENTER><B>Wygenerowane programem TurboWieszcz++</B>&nbsp;&nbsp;&nbsp;&nbsp;
(c)1997 <A HREF=\"mailto:kuba\@matrix.com.pl\">MoNsTeR</A>&amp; Danone.
&nbsp;Wszelkie prawa, itd...</CENTER>
</BODY></HTML>\n";

exit;

#############################################################################

### convert hex to ascii

sub hex2asc
 {
  local ($inv) = @_;
  local ($outv, @s,@j);

  @s=split('',$inv);
  while ($#s >=0)
   {
    if ($s[0] eq '%')
     {
      push(@j, sprintf("%c",hex("$s[1]$s[2]")));
      shift(@s);
      shift(@s);
     }
    else
     {
      push(@j, $s[0]);
     }
    shift (@s);
   }
  $outv = join ('',@j);
  return $outv;
}

sub prt_rnd()
{
 local($rset,$ending)=@_;
 local($max,@lista,$n=0,@lrnd,$maxhop=40,$hop);

 if ($rset eq 0) {$max=$sl1; @lista=@list1; @lrnd=@lastrnd1;}
 elsif ($rset eq 1) {$max=$sl2; @lista=@list2; @lrnd=@lastrnd2;}
 elsif ($rset eq 2) {$max=$sl3; @lista=@list3; @lrnd=@lastrnd3;}
 elsif ($rset eq 3) {$max=$sl4; @lista=@list4; @lrnd=@lastrnd4;}
 elsif ($rset eq 4) {$max=$sl5; @lista=@list5; @lrnd=@lastrnd5;}

 $hop=0;
 do
  {
   $n = int(rand($max));
   $x = index("@lrnd", "-$n-");
   $hop++;
  }
 while (( $x >=0 ) && ($hop < $maxhop));

# print "<BR>$rym:$rset:$n:(@lrnd)";
 print "<BR>@lista[$n]$ending\n";
 push(@lrnd,"-$n-");

 if ($rset eq 0) {@lastrnd1=@lrnd;}
 elsif ($rset eq 1) {@lastrnd2=@lrnd;}
 elsif ($rset eq 2) {@lastrnd3=@lrnd;}
 elsif ($rset eq 3) {@lastrnd4=@lrnd;}
 elsif ($rset eq 4) {@lastrnd5=@lrnd;}

}
