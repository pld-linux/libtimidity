Summary:	MIDI to WAVE converted library
Summary(pl.UTF-8):	Biblioteka konwertująca MIDI do WAVE
Name:		libtimidity
Version:	0.1.0
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libtimidity/%{name}-%{version}.tar.bz2
# Source0-md5:	72173a1084df0c42f9daa7b4568ebd18
URL:		http://libtimidity.sourceforge.net/
# configure is broken and tries to test whether g++ will be used to compile C
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is based on the TiMidity decoder from SDL_sound library.
Purpose to create this library is to avoid unnecessary dependences.
SDL_sound requires SDL and some other libraries, that not needed to
process MIDI files. In addition libtimidity provides more suitable
API to work with MIDI songs, it enables to specify full path to the
timidity configuration file, and have function to retrieve meta data
from MIDI song.

%description -l pl.UTF-8
Ta biblioteka jest oparta na kodzie dekodera TiMidity z biblioteki
SDL_sound. Celem jej powstania było uniknięcie niepotrzebnych
zależności. SDL_sound wymaga SDL-a i kilku innych bibliotek, które
nie są potrzebne do przetwarzania plików MIDI. Ponadto libtimidity
udostępnia bardziej odpowiednie API do pracy z utworami MIDI, pozwala
na podawanie pełnej ściezki do pliku konfiguracyjnego timidity i ma
funkcje do uzyskiwania metadanych z utworu MIDI.

%package devel
Summary:	Header files for libtimidity library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtimidity
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libtimidity library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtimidity.

%package static
Summary:	Static libtimidity library
Summary(pl.UTF-8):	Statyczna biblioteka libtimidity
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtimidity library.

%description static -l pl.UTF-8
Statyczna biblioteka libtimidity.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES ChangeLog NEWS README* TODO
%attr(755,root,root) %ghost %{_libdir}/libtimidity-*.so.0
%attr(755,root,root) %{_libdir}/libtimidity-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtimidity.so
%{_libdir}/libtimidity.la
%{_includedir}/timidity.h
%{_pkgconfigdir}/libtimidity.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtimidity.a
