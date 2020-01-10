Name:           meanwhile
Version:        1.1.0
Release:        12%{?dist}
Summary:        Lotus Sametime Community Client library
License:        LGPLv2+
URL:            http://%{name}.sourceforge.net

# The source for this package was pulled from upstream's vcs.  Use the following
# commands to generate the tarball:
# cvs -d:pserver:anonymous@%{name}.cvs.sourceforge.net:/cvsroot/%{name} login
# [hit return for the password]
# cvs -d:pserver:anonymous@%{name}.cvs.sourceforge.net:/cvsroot/%{name} co -d %{name}-1.1.0 -r %{name}_v1_1_0 %{name}
# cd %{name}-1.1.0
# ./autogen.sh
# make dist
Source:         %{name}-%{version}.tar.gz
Patch0:         %{name}-crash.patch
Patch1:         %{name}-fix-glib-headers.patch
Patch2:         %{name}-file-transfer.patch
Patch3:         %{name}-status-timestamp-workaround.patch
Patch4:         %{name}-aarch64.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  glib2-devel
BuildRequires:  doxygen

%description
The heart of the %{name} Project is the %{name} library, providing the basic
Lotus Sametime session functionality along with the core services; Presence
Awareness, Instant Messaging, Multi-user Conferencing, Preferences Storage,
Identity Resolution, and File Transfer.

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name}, you
will need to install %{name}-devel.

%package doc
Summary:        Documentation for the %{name} library
License:        GFDL

%description doc
Documentation for the %{name} library.

%prep
%setup -q
%patch0 -p0 -b .crash
%patch1 -p1 -b .fix-glib-headers
%patch2 -p1 -b .file-transfer
%patch3 -p1 -b .status-timestamp-workaround
%patch4 -p1 -b .aarch64

%build
%configure --enable-doxygen
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
# Remove the latex documentation.  Nobody reads it, it installs a font for
# some unknown reason, and people have to build it themselves.  Dumb.
rm -rf %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/latex \
    %{buildroot}%{_libdir}/lib%{name}.a \
    %{buildroot}%{_libdir}/lib%{name}.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING README TODO LICENSE NEWS
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%{_datadir}/doc/%{name}-doc-%{version}/

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.1.0-12
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.0-11
- Mass rebuild 2013-12-27

* Tue Mar 26 2013 Simone Caronni <negativo17@gmail.com> - 1.1.0-10
- Added aarch64 patch.

* Tue Mar 26 2013 Simone Caronni <negativo17@gmail.com> - 1.1.0-9
- Added patches for file transfer and status time workaround:
  http://www.lilotux.net/~mikael/pub/meanwhile/
- Spec file formatting.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Josh Boyer <jwboyer@gmail.com> 1.1.0-5
- Fix glib.h build issues (rhbz 750023)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 29 2010 Josh Boyer <jwboyer@gmail.com> - 1.1.0-4
- Remove lib%{name}.a (#556084)

* Tue Jan 12 2010 Dan Winship <danw@redhat.com> - 1.1.0-3
- Fix Source tag to indicate a CVS snapshot build.
- Resolves: #554446

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Josh Boyer <jwboyer@gmail.com> - 1.1.0-1
- Update to %{name}_v1_1_0 branch from upstream CVS. Fixes bug 490088
