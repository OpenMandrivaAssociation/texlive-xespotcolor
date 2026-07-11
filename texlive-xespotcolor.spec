%global tl_name xespotcolor
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Spot colours support for XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/xespotcolor
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xespotcolor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xespotcolor.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xespotcolor.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros for using spot colours in LaTeX documents.
The package is a reimplementation of the spotcolor package for use with
XeLaTeX. As such, it has the same user interface and the same
capabilities.

