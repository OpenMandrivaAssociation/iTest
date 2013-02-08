Summary: Testing system
Name: iTest
Version: 1.4.1
Release: 2
License: GPL
Group: Education
URL: http://itest.sourceforge.net/
Source: %{name}-%{version}-src.tar.gz
Patch0:	 itest-1.4-qt4.7.diff

BuildRequires: qt4-common qt4-devel

%description
iTest is a client-server appplication for creation and running tests and exams.

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


%changelog
* Wed Dec 29 2010 Александр Казанцев <kazancas@mandriva.org> 1.4.1-1mdv2011.0
+ Revision: 625744
- fix build for Qt4.7
-initial release
- import iTest


* Wed Apr 15 2009 Alexander Kazancev <kazancas@mandriva.ru> - 1.4.1-1
- version 1.4.1

* Fri Jan 09 2009 Alexander Kazancev <kazancas@mandriva.ru> - 1.4.0-1
- new release 1.4.0 for 2009.0
- fix spec for build of source code

* Wed May 28 2008 Alexander Kazancev <kazancas@mandriva.ru> - 1.3.0-2
- fix bug on disapear test windows

* Fri May 08 2008 Alexander Kazancev <kazancas@mandriva.ru> - 1.3.0-1
- packet for 2008.1

* Thu Nov 20 2007 Alexander Kazancev <kazancas@mandriva.ru> - 1.3.0-1
- Initial release.
