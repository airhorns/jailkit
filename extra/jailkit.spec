# $Id: jailkit.spec,v 1.1 2012/08/02 19:43:28 oli4 Exp $
# Authority: dag

Summary: Utilities to limit user accounts to specific files using chroot()
Name: jailkit
Version: 2.15
Release: 1.n247
License: Open Source
Group: System Environment/Base
URL: http://olivier.sessink.nl/jailkit/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://olivier.sessink.nl/jailkit/jailkit-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python

%description
Jailkit is a set of utilities to limit user accounts to specific files
using chroot() and or specific commands. Setting up a chroot shell,
a shell limited to some specific command, or a daemon inside a chroot
jail is a lot easier using these utilities.

Jailkit has been in use for a while on CVS servers (in a chroot and
limited to cvs), sftp/scp servers (both in a chroot and limited to
sftp/scp as well as not in a chroot but only limited to sftp/scp),
and also on general servers with accounts where the shell accounts
are in a chroot.

%prep
%setup -n %{name}-%{version}

### Disable broken Makefile :(
%{__perl} -pi.orig -e 's|>>||g' Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
	iniprefix="%{_sysconfdir}/jailkit/" \
	prefix="%{_prefix}"

%{__install} -Dp -m0755 extra/jailkit.centos %{buildroot}%{_initrddir}/jailkit

#%post
#cat /etc/shells | grep -v jk_chrootsh >/etc/shells
#echo "/usr/bin/jk_chrootsh" >> /etc/shells
#/sbin/chkconfig --add jailkit

#%postun
#cat /etc/shells | grep -v jk_chrootsh >/etc/shells

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)

%{_sbindir}/*
%{_bindir}/*

%{_datadir}/jailkit/

%doc %{_mandir}/man8/*
%config(noreplace) %{_sysconfdir}/jailkit
%config %{_initrddir}/jailkit





%changelog
* Mon Jul 16 2012 Jane Doe <who@127.0.0.1> - 2.15-1 
- Updated to release 2.15.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 2.1-1 - 4260+/thias
- Updated to release 2.1.

* Sun Mar 19 2006 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Fri May 20 2005 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
