Name:		texlive-refcount
Version:	53164
Release:	1
Summary:	Counter operations with label references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/refcount
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refcount.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refcount.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refcount.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides commands \setcounterref and \addtocounterref which use
the section (or whatever) number from the reference as the
value to put into the counter, as in: ...\label{sec:foo} ...
\setcounterref{foonum}{sec:foo} Commands \setcounterpageref and
\addtocounterpageref do the corresponding thing with the page
reference of the label. No .ins file is distributed; process
the .dtx with plain TeX to create one.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/refcount
%{_texmfdistdir}/tex/latex/refcount
%doc %{_texmfdistdir}/doc/latex/refcount

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
