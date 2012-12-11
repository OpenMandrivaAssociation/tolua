Name:           tolua
Summary:        A tool that greatly simplifies the integration of C/C++ code with Lua
Version:        5.1.2
Release:        %mkrel 1
License:        GPL
Group:          Development/Other
URL:            http://www.tecgraf.puc-rio.br/~celes/tolua/
Source0:        ftp://ftp.tecgraf.puc-rio.br/pub/users/celes/tolua/%{name}-%{version}.tar.gz
BuildRequires:	lua-devel
Requires:	lua >= 5.0.2
Provides:	tolua-devel
Requires:	%{name}-devel = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
tolua is a tool that greatly simplifies the integration of C/C++ 
code with Lua. Based on a cleaned header file, tolua automatically 
generates the binding code to access C/C++ features from Lua. 
Using Lua API and tag method facilities, tolua maps C/C++ constants, 
external variables, functions, classes, and methods to Lua.

%package -n %{name}-devel
Summary:	Header files for tolua
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Provides:	tolua-devel = %{version}-%{release}

%description -n %{name}-devel
Header files for tolua.

%prep
%setup -q -n %{name}-%{version}
find -name "*.o" | xargs rm
sed -i	-e "s@LUA=/usr/local@LUA=/usr@" \
	-e "s@LUALIB=$(LUA)/lib@LUALIB=$(LUA)/%{_lib}@" \
	-e "s@CFLAGS=@CFLAGS=%{optflags}@" \
	-e "s@CXXFLAGS=@CXXFLAGS=%{optflags}@" \
	config


%build
%make

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -m 755 bin/%{name} %{buildroot}%{_bindir}

install -dm 755 %{buildroot}%{_includedir}
install -m 644 include/%{name}.h %{buildroot}%{_includedir}

install -dm 755 %{buildroot}%{_libdir}
install -m 644 lib/lib%{name}.a %{buildroot}%{_libdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%files -n %{name}-devel
%defattr(-,root,root)
%doc INSTALL README
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a


%changelog
* Mon Aug 17 2009 Frederik Himpe <fhimpe@mandriva.org> 5.1.2-1mdv2010.0
+ Revision: 417403
- Update to new version 5.1.2
- Remove Mach binaries wrongly included in tarball
- Replace config patch by some sed hackery

* Mon Aug 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 5.1b-1mdv2009.0
+ Revision: 275905
- update to new version 5.1b
- drop patch0, fixed upstream
- Patch1: adjust config options
- docs are gone now

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 5.0-3mdv2009.0
+ Revision: 242860
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jun 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 5.0-1mdv2008.0
+ Revision: 40423
- provide patch 1 (fix compatability with Lua 5.1)
- create devel subpackage
- spec file clean
- Import tolua

