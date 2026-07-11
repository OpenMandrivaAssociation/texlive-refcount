%global tl_name refcount
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.6
Release:	%{tl_revision}.1
Summary:	Counter operations with label references
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/refcount
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refcount.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refcount.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refcount.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides commands \setcounterref and \addtocounterref which use the
section (or whatever) number from the reference as the value to put into
the counter, as in: ...\label{sec:foo} ...
\setcounterref{foonum}{sec:foo} Commands \setcounterpageref and
\addtocounterpageref do the corresponding thing with the page reference
of the label. No .ins file is distributed; process the .dtx with plain
TeX to create one.

