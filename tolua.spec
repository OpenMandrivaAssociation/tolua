Name:           tolua
Summary:        A tool that greatly simplifies the integration of C/C++ code with Lua
Version:        5.0
Release:        %mkrel 1
License:        GPL
Group:          Development/Other
URL:            http://www.tecgraf.puc-rio.br/~celes/tolua/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-make.diff
BuildRequires:	dos2unix
BuildRequires:	lua-devel
Requires:	lua >= 5.0.2
Provides:	tolua-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
tolua


%prep
%setup -q -n %{name}-%{version}
%patch -p1

dos2unix  doc/*.html
chmod 644 doc/*.html

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
%doc INSTALL README doc/
%{_bindir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a
