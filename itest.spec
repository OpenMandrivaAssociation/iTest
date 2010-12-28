Summary: Testing system
Name: iTest
Version: 1.4.1
Release: %mkrel 1
License: GPL
Group: Education
URL: http://itest.sourceforge.net/
Source: %{name}-%{version}-src.tar.gz
Patch0:	 itest-1.4-qt4.7.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt4-common qt4-devel

%description
iTest - it is a client-server appplication for create and execution tests and exams. 
This may work by server on a one computer and many mashine for student may connect for it

%prep
%setup -qn %{name}-%{version}-src -q
%patch0 -p1

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
rm -rf %{buildroot}

install -m 755 -d %{buildroot}%{_bindir}
install -m 755 bin/iTestClient $RPM_BUILD_ROOT%{_bindir}
install -m 755 bin/iTestServer $RPM_BUILD_ROOT%{_bindir}
install -m 755 -d %{buildroot}%{_iconsdir}
install -m 644 *.png $RPM_BUILD_ROOT%{_iconsdir}

%makeinstall

install -dm 755 %{buildroot}%{_datadir}/applications
cat > itest.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
GenericName=iTests & iExams
GenericName[ru]=Экзаменатор iTest
Comment=iTest -  Tests & Exams Program by Qt4
Comment[ru]=Мощная программа для проведения тестов
Exec=%{_bindir}/iTestServer
Icon=%{_iconsdir}/itdb.png
MimeType=application/x-edu;application/x-edugallery
Name=iTestServer
DocPath=
Path=%{_bindir}
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
Exec=%{_bindir}/iTestClient
Icon=%{_iconsdir}/itos.png
MimeType=application/x-edu;application/x-edugallery
Name=iTestClient
DocPath=
Path=%{_bindir}
Terminal=false
Type=Application
X-DCOP-ServiceType=Multi
Categories=Qt;KDE;Education;Teaching;X-MandrivaLinux-MoreApplications-Education-Other;
EOF
install -m 0644 itestwri.desktop \
%{buildroot}%{_datadir}/applications/itestwri.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root, root)
%{_bindir}/iTestClient
%{_bindir}/iTestServer
%{_iconsdir}/itcl.png
%{_iconsdir}/itdb.png
%{_iconsdir}/itest.png
%{_iconsdir}/itestwri.png
%{_iconsdir}/itos.png
%{_datadir}/applications/itest.desktop
%{_datadir}/applications/itestwri.desktop
