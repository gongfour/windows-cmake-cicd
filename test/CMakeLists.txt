set(TESTS
    test_liba
)

foreach(test_name IN LISTS TESTS)
    add_executable(${test_name} ${test_name}.cpp)
    target_link_libraries(${test_name} PRIVATE liba)
    add_test(NAME ${test_name} COMMAND $<TARGET_FILE:${test_name}>)
endforeach()