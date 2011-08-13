Summary:	vrrpd - an implementation of VRRPv2
Summary(pl.UTF-8):	vrrpd - implementacja protokołu VRRPv2
Name:		vrrpd
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/vrrpd/%{name}-%{version}.tar.gz
# Source0-md5:	6d5066ea1a6ced817376ca0f54765447
URL:		http://sourceforge.net/apps/trac/vrrpd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{name} is an implementation of VRRPv2 as specified in RFC 2338. It
run in userspace for Linux. In short, VRRP is a protocol which elects
a master server on a LAN. If the master fails, a backup server takes
over.

%description -l pl.UTF-8
%{name} to implementacja protokołu VRRPv2, którego specyfikacja
znajduje się w RFC 2338. Uruchamiany jest w przestrzeni użytkownika.
W skrócie: protokół VRRP wybiera serwer nadrzędny w sieci LAN. Jeżeli
on zawiedzie, serwer pomocniczy przejmuje jego funkcje.

%prep
%setup -q

%build
%{__make} clean
%{__make} \
	CC="%{__cc}" \
	CPPFLAGS="%{rpmcppflags}" \
	DBG_OPT="%{rpmcflags}" \
	LINKLIB="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install vrrpd $RPM_BUILD_ROOT%{_sbindir}
install vrrpd.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes FAQ route.generic TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
