from conans import ConanFile, CMake, tools


class LibaConan(ConanFile):
    name = "liba"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/gongfour/windows-cmake-cicd"
    author = "kangwonjin kangwonjin.dev@gmail.com"
    exports_sources = [
        "include/**",
        "source/**",
        "test/**",
        "CMakeLists.txt"
    ]

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
