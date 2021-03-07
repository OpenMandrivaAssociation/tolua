Name:           tolua
Summary:        A tool that greatly simplifies the integration of C/C++ code with Lua
Version:        5.2.4
Release:        1
License:        GPL
Group:          Development/Other
URL:            http://www.tecgraf.puc-rio.br/~celes/tolua/
Source0:        ftp://ftp.tecgraf.puc-rio.br/pub/users/celes/tolua/%{name}-%{version}.tar.gz
BuildRequires:	lua-devel
Requires:	lua >= 5.0.2
Requires:	%{name}-devel = %{EVRD}

%description
tolua is a tool that greatly simplifies the integration of C/C++ 
code with Lua. Based on a cleaned header file, tolua automatically 
generates the binding code to access C/C++ features from Lua. 
Using Lua API and tag method facilities, tolua maps C/C++ constants, 
external variables, functions, classes, and methods to Lua.

%package -n %{name}-devel
Summary:	Header files for tolua
Group:		Development/Other
Requires:	%{name} = %{EVRD}
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
install -dm 755 %{buildroot}%{_bindir}
install -m 755 bin/%{name} %{buildroot}%{_bindir}

install -dm 755 %{buildroot}%{_includedir}
install -m 644 include/%{name}.h %{buildroot}%{_includedir}

install -dm 755 %{buildroot}%{_libdir}
install -m 644 lib/lib%{name}.a %{buildroot}%{_libdir}

%files
%{_bindir}/%{name}

%files -n %{name}-devel
%doc INSTALL README
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a

