Summary:	MIDI to WAVE converted library
Summary(pl.UTF-8):	Biblioteka konwertująca MIDI do WAVE
Name:		libtimidity
Version:	0.2.6
Release:	1
License:	LGPL v2.1+ or GPL v2+ or Artistic
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libtimidity/%{name}-%{version}.tar.gz
# Source0-md5:	ae4264b776c55ad0aee7fb76702f1b2d
URL:		http://libtimidity.sourceforge.net/
# for noinst program
#BuildRequires:	libao-devel
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
%doc AUTHORS CHANGES COPYING README* TODO
%attr(755,root,root) %{_libdir}/libtimidity.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtimidity.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtimidity.so
%{_libdir}/libtimidity.la
%{_includedir}/timidity.h
%{_pkgconfigdir}/libtimidity.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtimidity.a
