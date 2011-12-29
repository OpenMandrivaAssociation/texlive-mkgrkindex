# revision 18835
# category Package
# catalog-ctan /language/greek/mkgrkindex
# catalog-date 2009-07-22 21:50:16 +0200
# catalog-license other-free
# catalog-version 2.0
Name:		texlive-mkgrkindex
Version:	2.0
Release:	1
Summary:	Makeindex working with Greek
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/greek/mkgrkindex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkgrkindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkgrkindex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-mkgrkindex.bin = %{EVRD}

%description
Makeindex is resolutely stuck with Latin-based alphabets, so
will not deal with Greek indexes, unaided. This package
provides a Perl script that will transmute the index of a Greek
document in such a way that makeindex will sort the entries
according to the rules of the Greek alphabet.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mkgrkindex
%{_texmfdistdir}/makeindex/mkgrkindex/lowercase-headers.ist
%{_texmfdistdir}/makeindex/mkgrkindex/uppercase-headers.ist
%{_texmfdistdir}/scripts/mkgrkindex/mkgrkindex
%doc %{_texmfdistdir}/doc/support/mkgrkindex/mkgrkindex.nw
%doc %{_texmfdistdir}/doc/support/mkgrkindex/mkgrkindex.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/mkgrkindex/mkgrkindex mkgrkindex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
