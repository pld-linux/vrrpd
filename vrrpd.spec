Summary:	vrrpd is an implementation of VRRPv2
Summary(pl):	vrrpd to implementacja protoko³u VRRPv2
Name:		vrrpd
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.off.net/~jme/%{name}/%{name}-%{version}.tgz
URL:		http://www.off.net/~jme/vrrpd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{name} is an implementation of VRRPv2 as specified in rfc2338. It run
in userspace for linux. In short, VRRP is a protocol which elects a
master server on a LAN. If the master fails, a backup server takes
over.

%description -l pl
%{name} to implementacja protoko³u VRRPv2, którego specyfikacja
znjduje sie w rfc2338. Uruchamiany jest w przestrzeniu u¿ytkownika. Po
krótce, protokó³ vrrp wybiera serwer masrer w sieci LAN. Je¿eli master
zawiedzie, serwer pomocniczy przejmuje jego funkcje

%prep
%setup -q -n %{name}

%build

%{__make} clean
%{__make} \
	CPPFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d   $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install vrrpd $RPM_BUILD_ROOT%{_sbindir}
install vrrpd.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes FAQ route.generic TODO
%attr(755,root,root) %{_sbindir}
%{_mandir}/man8/*
