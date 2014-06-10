%define		_state		stable
%define		orgname		kmines
%define		qtver		4.8.0

Summary:	KDE minesweeper game
Summary(pl.UTF-8):	Saper dla KDE
Summary(pt_BR.UTF-8):	Versão do jogo 'caça-minas' para o KDE
Name:		kde4-%{orgname}
Version:	4.13.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	5bf52e5ecd3240dbe264618068554cd7
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very classical minesweeper written from scratch.
- 3 predefined levels (Easy: 8x8 with 10 mines, Normal: 16x16 with 40
  mines, Expert: 30x16 with 99 mines)
- Custom levels
- High Scores.

%description -l pl.UTF-8
Wersja klasycznej gry "saper" dla KDE, napisana od zera. Cechy:
- 3 predefiniowane poziomy (łatwy - 8x8 z 10 minami, normalny - 16x16
  z 40 minami, dla ekspertów - 30x16 z 99 minami)
- definiowalne poziomy
- lista najlepszych wyników.

%description -l pt_BR.UTF-8
Versão do jogo 'caça-minas' para o KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmines
%{_desktopdir}/kde4/kmines.desktop
%{_datadir}/apps/kmines
%{_datadir}/config/kmines.knsrc
%{_iconsdir}/*/*/apps/kmines.png
