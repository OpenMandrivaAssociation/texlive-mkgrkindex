%global tl_name mkgrkindex
%global tl_revision 26313

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Makeindex working with Greek
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/greek/mkgrkindex
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mkgrkindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mkgrkindex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(mkgrkindex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Makeindex is resolutely stuck with Latin-based alphabets, so will not
deal with Greek indexes, unaided. This package provides a Perl script
that will transmute the index of a Greek document in such a way that
makeindex will sort the entries according to the rules of the Greek
alphabet.

