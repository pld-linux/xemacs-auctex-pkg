### Comment
# This file is modified automatically by 'xemacs-adapter' script
# from PLD-project CVS repository: cvs.pld.org.pl, module SPECS
# For more details see comments in this script
### EndComment

Summary:	Tex editing mode for xemacs
Summary(pl):	Tryb TeXowy dla xemacsa

Name:    	xemacs-auctex-pkg
%define 	srcname	auctex
Version: 	1.17
Release:	1

### Preamble
Copyright:	GPL
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:      	http://www.xemacs.org
Source:   	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires: 	xemacs
Requires: 	xemacs-base-pkg
### EndPreamble

%description


%description -l pl 


%package el
Summary:	.el source files for XEmacs
Summary(pl):	Pliki ¼ród³owe procedur w eLispie do XEmacsa

### ElPreamble
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires: 	%{name} = %{version}
### EndElPreamble


%description el
.el source files -- not necessary to run XEmacs

%description el -l pl
Pliki ¼ród³owe procedur w eLispie do XEmacsa.


### Main
%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
install -d $RPM_BUILD_ROOT%{_infodir}
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info
### EndMain

### PrePost
%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
### EndPrePost

### Files
%files
%{_datadir}/xemacs-packages/etc/*
%{_infodir}/*
%{_datadir}/xemacs-packages/lisp/*
### EndFiles
