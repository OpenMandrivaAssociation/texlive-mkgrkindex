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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Makeindex is resolutely stuck with Latin-based alphabets, so
will not deal with Greek indexes, unaided. This package
provides a Perl script that will transmute the index of a Greek
document in such a way that makeindex will sort the entries
according to the rules of the Greek alphabet.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mkgrkindex
%{_texmfdistdir}/makeindex/mkgrkindex/lowercase-headers.ist
%{_texmfdistdir}/makeindex/mkgrkindex/uppercase-headers.ist
%{_texmfdistdir}/scripts/mkgrkindex/mkgrkindex
%doc %{_texmfdistdir}/doc/support/mkgrkindex/mkgrkindex.nw
%doc %{_texmfdistdir}/doc/support/mkgrkindex/mkgrkindex.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

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
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
