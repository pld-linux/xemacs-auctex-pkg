Summary:	Basic TeX/LaTeX support
Summary(pl):	Podstawowe wsparcie dla TeXa/LaTeXa
Name:		xemacs-auctex-pkg
%define 	srcname	auctex
Version:	10.0g
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
# new versions here:
# http://savannah.gnu.org/download/auctex/stable.pkg/%{version}/%{srcname}-%{version}.tar.gz
Source0:	http://savannah.gnu.org/download/auctex/attic/auctex/%{srcname}-%{version}.tar.gz
# Source0-md5:	5b115bf49f79b63b9a71dec3301c4707
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/auctex/
BuildArch:	noarch
BuildRequires:	xemacs
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	xemacs

%description
AUC TeX is a comprehensive customizable integrated environment for
writing input files for LaTeX using GNU Emacs and XEmacs.

AUC TeX lets you run TeX/LaTeX and other LaTeX-related tools, such as
a output filters or post processor from inside [X]Emacs. Especially
"Running LaTeX" is interesting, as AUC TeX lets you browse through the
errors TeX reported, while it moves the cursor directly to the
reported error, and displays some documentation for that particular
error. This will even work when the document is spread over several
files.

AUC TeX automatically indents your "LaTeX-source", not only as you
write it -- you can also let it indent and format an entire document.
It has a special outline feature, which can greatly help you getting
an overview of a document.

Apart from these special features, AUC TeX provides a large range of
handy [X]Emacs macros, which in several different ways can help you
write your LaTeX documents fast and painlessly.

%description -l pl
AUC TeX jest kompletnym i konfigurowalnym �rodowiskiem edycji plik�w
�r�d�owych LaTeXa, dost�pnym w programach GNU Emacs i XEmacs.

AUC TeX umo�liwia uruchamianie narz�dzi pakietu TeX/LaTeX i innych,
takich jak konwertery czy filtry z wewn�trz programu [X]Emacs.
Szczeg�lnie interesuj�ca jest opcja "Running LaTeX", poniewa� pozwala
ona przegl�da� wiadomo�ci o b��dach w plikach �r�d�owych, przesuwa�
kursor od razu w miejsce wyst�pienia b��du i czyta� pliki dokumentacji
dotycz�ce tego b��du. Funkcja dzia�a poprawnie nawet dla dokument�w
sk�adaj�cych si� z kilku plik�w �r�d�owych.

AUC TeX w spos�b automatyczny formatuje plik �r�d�owy LaTeXa, zar�wno
na bie��co jak i po wpisaniu. Posiada specjaln� funkcj� "zarysu
dokumentu", kt�ra wydatnie pomaga przegl�da� dokumenty.

Poza powy�szymi specja�ami, AUC TeX dostarcza wiele u�ytecznych makr,
pomocnych w szybkiej i bezbolesnej edycji dokument�w LaTeXa.

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

%build
(cd doc; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)
%{__make} EMACS=xemacs


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

%{__make} install \
	lispdir=$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp
perl -pi -e "s#$RPM_BUILD_ROOT##" $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/tex-site.el

install doc/*.info* $RPM_BUILD_ROOT%{_infodir}

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/auctex
%{_datadir}/xemacs-packages/lisp/auctex/*.el*
%dir %{_datadir}/xemacs-packages/lisp/auctex/style
%{_datadir}/xemacs-packages/lisp/auctex/style/*.el*
%{_datadir}/xemacs-packages/lisp/tex-site.el
%{_infodir}/*
