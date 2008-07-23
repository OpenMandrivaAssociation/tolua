Name:           tolua
Summary:        A tool that greatly simplifies the integration of C/C++ code with Lua
Version:        5.0
Release:        %mkrel 3
License:        GPL
Group:          Development/Other
URL:            http://www.tecgraf.puc-rio.br/~celes/tolua/
Source0:        ftp://ftp.tecgraf.puc-rio.br/pub/users/celes/tolua/%{name}-%{version}.tar.bz2
Patch0:         %{name}-5.0-fixes.patch
BuildRequires:	dos2unix
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
%patch -p1

dos2unix  doc/*.html
chmod 644 doc/*

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
%doc INSTALL README doc/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a
