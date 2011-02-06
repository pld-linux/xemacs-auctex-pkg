%define 	srcname	auctex
Summary:	Basic TeX/LaTeX support
Summary(pl.UTF-8):	Podstawowe wsparcie dla TeXa/LaTeXa
Name:		xemacs-auctex-pkg
Version:	11.83
Release:	0.1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.gnu.org/pub/gnu/auctex/%{srcname}-%{version}.tar.gz
# Source0-md5:	19480487036f602841507c0e151674c2
#Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/auctex/
BuildRequires:	texinfo
BuildRequires:	xemacs >= 21.4.9
BuildRequires:	xemacs-texinfo-pkg
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
AUC TeX jest kompletnym i konfigurowalnym środowiskiem edycji plików
źródłowych LaTeXa, dostępnym w programach GNU Emacs i XEmacs.

AUC TeX umożliwia uruchamianie narzędzi pakietu TeX/LaTeX i innych,
takich jak konwertery czy filtry z wewnątrz programu [X]Emacs.
Szczególnie interesująca jest opcja "Running LaTeX", ponieważ pozwala
ona przeglądać wiadomości o błędach w plikach źródłowych, przesuwać
kursor od razu w miejsce wystąpienia błędu i czytać pliki dokumentacji
dotyczące tego błędu. Funkcja działa poprawnie nawet dla dokumentów
składających się z kilku plików źródłowych.

AUC TeX w sposób automatyczny formatuje plik źródłowy LaTeXa, zarówno
na bieżąco jak i po wpisaniu. Posiada specjalną funkcję "zarysu
dokumentu", która wydatnie pomaga przeglądać dokumenty.

Poza powyższymi specjałami, AUC TeX dostarcza wiele użytecznych makr,
pomocnych w szybkiej i bezbolesnej edycji dokumentów LaTeXa.

%define texhash [ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

%package -n xemacs-preview-latex
Summary:	Embedded LaTeX previewer for XEmacs
Summary(pl.UTF-8):	Osadzona przeglądarka pre-renderująca kod LaTeXowy w XEmacsie
Group:		Applications/Editors/XEmacs
Requires(post,postun):	%{_bindir}/texhash
Requires:	ghostscript >= 6.51
Requires:	ghostscript >= 6.51
Requires:	tetex-dvips
Requires:	tetex-format-latex
Requires:	xemacs >= 21.4.9
Requires:	%{name} = %{version}-%{release}
Obsoletes:	xemacs-preview-latex-pkg

%description -n xemacs-preview-latex
Does your neck hurt from turning between previewer windows and the
source too often? This Elisp/LaTeX package will render your displayed
LaTeX equations right into the editing window where they belong.

%description -n xemacs-preview-latex -l pl.UTF-8
Czy Ciebie też boli szyja od ciągłego przenoszenia wzroku z okienka
podglądu na edytor źródła dokumentu? Ten pakiet napisany w
Elisp/LaTeXu wyświetli końcową postać równań LaTeXa tam, gdzie trzeba
- w oknie edytora.

%prep
%setup -q -n %{srcname}-%{version}
#%patch0 -p1

%build
%configure \
	--with-xemacs \
	--with-lispdir=%{_datadir}/xemacs-packages/lisp \
	--with-packagedir=%{_datadir}/xemacs-packages \
	--with-tex-input-dir="%{_datadir}/texmf/tex;%{_datadir}/texmf/bibtex/bst"
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# movig info and dvi files that are installed not in the proper place
install -d $RPM_BUILD_ROOT%{_infodir}
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/preview
mv $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/* $RPM_BUILD_ROOT%{_infodir}
mv $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/styles/preview.dvi $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/preview
# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post -n xemacs-preview-latex
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
%texhash

%postun -n xemacs-preview-latex
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
%texhash

%files
%defattr(644,root,root,755)
%doc README ChangeLog CHANGES
%dir %{_datadir}/xemacs-packages/lisp/auctex
%{_datadir}/xemacs-packages/lisp/auctex/*.el*
%exclude %{_datadir}/xemacs-packages/lisp/auctex/preview*
%{_datadir}/xemacs-packages/etc/auctex
%{_datadir}/xemacs-packages/pkginfo/MANIFEST.auctex
%{_infodir}/auctex.info*

%files -n xemacs-preview-latex
%defattr(644,root,root,755)
%{_infodir}/preview-latex.info*
%{_datadir}/texmf/tex/latex/preview/*
%{_datadir}/texmf/doc/latex/preview
%{_datadir}/xemacs-packages/lisp/auctex/preview*
