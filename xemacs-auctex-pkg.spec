Summary:	Basic TeX/LaTeX support
Summary(pl):	Basic TeX/LaTeX support
Name:		xemacs-auctex-pkg
%define 	srcname	auctex
Version:	9.9p
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.icm.edu.pl/pub/CTAN/support/auctex/%{srcname}-%{version}.tar.gz
Patch0:		%{name}-info.patch
##URL:		http://www.xemacs.org/
BuildArch:	noarch
##Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	xemacs

%description

%description -l pl 

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

%build
(cd doc; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)
%{__make} EMACS=xemacs


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

%{__make} lispdir=$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp install
perl -pi -e "s#$RPM_BUILD_ROOT##" $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/tex-site.el

mv -f  doc/*.info* $RPM_BUILD_ROOT%{_infodir}


#cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
#mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
#rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info* \
	README ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/auctex
%{_datadir}/xemacs-packages/lisp/auctex/*.elc
%{_datadir}/xemacs-packages/lisp/auctex/style/*.elc
%{_datadir}/xemacs-packages/lisp/tex-site.el
%doc README.gz ChangeLog.gz 
