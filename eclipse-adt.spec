# TODO
# - how to (where to?) package web and xml and index.html
Summary:	ADT Plugin for Eclipse
Name:		eclipse-adt
Version:	22.0.5
Release:	1
License:	EPL v1.0
Group:		Libraries/Java
Obsoletes:	eclipse-plugin-adt
Source0:	http://dl.google.com/android/ADT-%{version}.zip
# Source0-md5:	1097fccf32063e3638a9d27aa0f295ca
URL:		http://developer.android.com/sdk/eclipse-adt.html
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	eclipse >= 3.6.2
Requires:	eclipse-gef
Requires:	eclipse-jdt
Requires:	eclipse-plugin-webtools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipsedir	%{_libdir}/eclipse/dropins/adt

%description
Android Development Tools (ADT) is a plugin for the Eclipse IDE that
is designed to give you a powerful, integrated environment in which to
build Android applications.

%prep
%setup -qc
find -name '*.jar' | while read jar; do
	dir=${jar%.jar}
	install -d $dir
	%{__unzip} -qq $jar -d $dir
	rm $jar
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}

cp -a features/* $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a plugins/* $RPM_BUILD_ROOT%{eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{eclipsedir}
%dir %{eclipsedir}/features
%dir %{eclipsedir}/plugins
%{eclipsedir}/features/com.android.ide.eclipse.*
%{eclipsedir}/plugins/com.android.ide.eclipse.*
%{eclipsedir}/plugins/overlay.com.android.ide.eclipse.adt.*
