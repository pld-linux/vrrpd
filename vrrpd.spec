Summary:	vrrpd - an implementation of VRRPv2
Summary(pl):	vrrpd - implementacja protoko³u VRRPv2
Name:		vrrpd
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.off.net/~jme/%{name}/%{name}-%{version}.tgz
# Source0-md5:	b66aa188e71b082d581ae84b2a380cad
URL:		http://www.off.net/~jme/vrrpd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{name} is an implementation of VRRPv2 as specified in RFC 2338. It
run in userspace for Linux. In short, VRRP is a protocol which elects
a master server on a LAN. If the master fails, a backup server takes
over.

%description -l pl
%{name} to implementacja protoko³u VRRPv2, którego specyfikacja
znajduje siê w RFC 2338. Uruchamiany jest w przestrzeni u¿ytkownika.
W skrócie: protokó³ VRRP wybiera serwer nadrzêdny w sieci LAN. Je¿eli
on zawiedzie, serwer pomocniczy przejmuje jego funkcje.

%prep
%setup -q -n %{name}

%build
%{__make} clean
%{__make} \
	CPPFLAGS="%{rpmcflags}"

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
