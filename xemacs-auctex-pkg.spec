Summary:	Basic TeX/LaTeX support
Summary(pl):	Podstawowe wsparcie dla TeXa/LaTeXa
Name:		xemacs-auctex-pkg
%define 	srcname	auctex
Version:	11.53
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
# new versions here:
# http://savannah.gnu.org/download/auctex/stable.pkg/%{version}/%{srcname}-%{version}.tar.gz
Source0:	ftp://ftp.gnu.org/pub/gnu/auctex/%{srcname}-%{version}.tar.gz
# Source0-md5:	938ba7debc040c6bdb6d891706d17dcc
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/auctex/
BuildArch:	noarch
BuildRequires:	xemacs
BuildRequires:	texinfo
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
AUC TeX jest kompletnym i konfigurowalnym ¶rodowiskiem edycji plików
¼ród³owych LaTeXa, dostêpnym w programach GNU Emacs i XEmacs.

AUC TeX umo¿liwia uruchamianie narzêdzi pakietu TeX/LaTeX i innych,
takich jak konwertery czy filtry z wewn±trz programu [X]Emacs.
Szczególnie interesuj±ca jest opcja "Running LaTeX", poniewa¿ pozwala
ona przegl±daæ wiadomo¶ci o b³êdach w plikach ¼ród³owych, przesuwaæ
kursor od razu w miejsce wyst±pienia b³êdu i czytaæ pliki dokumentacji
dotycz±ce tego b³êdu. Funkcja dzia³a poprawnie nawet dla dokumentów
sk³adaj±cych siê z kilku plików ¼ród³owych.

AUC TeX w sposób automatyczny formatuje plik ¼ród³owy LaTeXa, zarówno
na bie¿±co jak i po wpisaniu. Posiada specjaln± funkcjê "zarysu
dokumentu", która wydatnie pomaga przegl±daæ dokumenty.

Poza powy¿szymi specja³ami, AUC TeX dostarcza wiele u¿ytecznych makr,
pomocnych w szybkiej i bezbolesnej edycji dokumentów LaTeXa.

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

%build
%configure --with-xemacs \
	   --with-lispdir=%{_datadir}/xemacs-packages/lisp \
	   --with-packagedir=%{_datadir}/xemacs-packages \
	   --with-tex-input-dir="%{_datadir}/texmf/tex;%{_datadir}/texmf/bibtex/bst"
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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
%doc README ChangeLog CHANGES
%dir %{_datadir}/xemacs-packages/lisp/auctex
%{_datadir}/xemacs-packages/lisp/auctex/*.el*
%dir %{_datadir}/xemacs-packages/lisp/auctex/style
%{_datadir}/xemacs-packages/lisp/auctex/style/*.el*
%{_datadir}/xemacs-packages/lisp/tex-site.el
%{_infodir}/*
