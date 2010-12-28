# $Id: itest.spec 5762 2007-08-20 18:35:39Z dries $
# Authority: akdengi
# Upstream: itest.sourceforge.net
%define rel 1

%{?dist: %{expand: %%define %dist 1}}

Summary: Testing system
Name: iTest
Version: 1.4.1
Release: %mkrel %{rel}
License: GPL
Group: Education
URL: http://itest.sourceforge.net/

Packager: Alexander Kazancev <kazancas@mail.ru>
Vendor: Mandriva Russia, http://www.mandriva.ru

Source: %{name}-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt4-common

%description
iTest - it is a client-server appplication for create and execution tests and exams. 
This may work by server on a one computer and many mashine for student may connect for it

%description -l ru
iTest - это клиент-серверное приложение для создания и проведения тестов и экзаменов.
Он может работать как сервер на одной машине или к нему можно подключить множество компьютеров.

%post
ln -s /opt/iTest-%{version}/iTestServer /usr/bin/iTest
ln -s /opt/iTest-%{version}/iTestClient /usr/bin/iTestWri

%postun
rm -rf /usr/bin/iTest
rm -rf /usr/bin/iTestWri

%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%setup -n %{name}-%{version}-src -q

%build
cd iTestServer
%qmake_qt4 -config release
%qt4bin/lrelease iTestServer.pro
cd ..
cd iTestClient
%qmake_qt4 -config release
%qt4bin/lrelease iTestClient.pro
cd ..
%qmake_qt4 -config release
make

%install
mkdir $RPM_BUILD_ROOT/opt
mkdir $RPM_BUILD_ROOT/opt/iTest-%{version}
mkdir $RPM_BUILD_ROOT/usr
mkdir $RPM_BUILD_ROOT/usr/bin
mkdir $RPM_BUILD_ROOT%{_datadir}
mkdir $RPM_BUILD_ROOT%{_datadir}/applications
cp -r bin/iTestClient $RPM_BUILD_ROOT/opt/iTest-%{version}
cp -r bin/iTestServer $RPM_BUILD_ROOT/opt/iTest-%{version}
cp -r *.png $RPM_BUILD_ROOT/opt/iTest-%{version}

%makeinstall

install -dm 755 %{buildroot}%{_datadir}/applications
cat > itest.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
GenericName=iTests & iExams
GenericName[ru]=Экзаменатор iTest
Comment=iTest -  Tests & Exams Program by Qt4
Comment[ru]=Мощная программа для проведения тестов
Exec=/opt/iTest-%{version}/iTestServer
Icon=/opt/iTest-%{version}/itdb.png
MimeType=application/x-edu;application/x-edugallery
Name=iTestServer
DocPath=
Path=/opt/iTest-%{version}/
Terminal=false
Type=Application
X-DCOP-ServiceType=Multi
Categories=Qt;KDE;Education;Teaching;X-MandrivaLinux-MoreApplications-Education-Other;
EOF
install -m 0644 itest.desktop \
%{buildroot}%{_datadir}/applications/itest.desktop

install -dm 755 %{buildroot}%{_datadir}/applications
cat > itestwri.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
GenericName=iTests & iExams client
GenericName[ru]=Клиент для экзаменатора iTest
Comment=iTest -  Tests & Exams client by Qt4
Comment[ru]=Клиент для проведения тестов iTest
Exec=/opt/iTest-%{version}/iTestClient
Icon=/opt/iTest-%{version}/itos.png
MimeType=application/x-edu;application/x-edugallery
Name=iTestClient
DocPath=
Path=/opt/iTest-%{version}/
Terminal=false
Type=Application
X-DCOP-ServiceType=Multi
Categories=Qt;KDE;Education;Teaching;X-MandrivaLinux-MoreApplications-Education-Other;
EOF
install -m 0644 itestwri.desktop \
%{buildroot}%{_datadir}/applications/itestwri.desktop

%files
%defattr(-,root, root)
/opt/iTest-%{version}/iTestClient
/opt/iTest-%{version}/iTestServer
/opt/iTest-%{version}/itcl.png
/opt/iTest-%{version}/itdb.png
/opt/iTest-%{version}/itest.png
/opt/iTest-%{version}/itestwri.png
/opt/iTest-%{version}/itos.png
%{_datadir}/applications/itest.desktop
%{_datadir}/applications/itestwri.desktop


