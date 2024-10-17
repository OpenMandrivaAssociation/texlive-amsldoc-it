Name:		texlive-amsldoc-it
Version:	45662
Release:	2
Summary:	TeXLive amsldoc-it package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsldoc-it.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsldoc-it.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive amsldoc-it package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/amsldoc-it/itamsldoc.pdf
%doc %{_texmfdistdir}/doc/latex/amsldoc-it/itamsldoc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
