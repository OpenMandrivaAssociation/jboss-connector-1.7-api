%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-connector-1.7-api
Version:          1.0.0
Release:          2.3
Summary:          Connector Architecture 1.7 API
Group:		  Development/Java
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org
Source0:          https://github.com/jboss/jboss-connector-api_spec/archive/jboss-connector-api_1.7_spec-%{namedversion}.tar.gz
Source1:          cddl.txt

BuildRequires:    jboss-parent
BuildRequires:    maven-local
BuildRequires:    maven-enforcer-plugin
BuildRequires:    jboss-transaction-1.2-api

BuildArch:        noarch

%description
Java EE Connector Architecture 1.7 API classes

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-connector-api_spec-jboss-connector-api_1.7_spec-%{namedversion}

cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc cddl.txt

%files javadoc -f .mfiles-javadoc
%doc cddl.txt

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-1
- Upstream release 1.0.0.Final

* Tue Oct 08 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.1.Beta1
- Initial packaging

