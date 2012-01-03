# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-amsldoc-it
Version:	20111103
Release:	2
Summary:	TeXLive amsldoc-it package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsldoc-it.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsldoc-it.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
